set ns [new Simulator]

set nr [open outu.tr w]
$ns trace-all $nr
set nf [open outu.nam w]

$ns namtrace-all $nf
proc finish {} {
global ns nr nf 
$ns flush-trace
close $nf
close $nr 
exec nam outu.nam
exit 0
}

for { set i 0 } { $i<4} { incr i 1 } {
set n($i) [$ns node]}

$ns duplex-link $n(0) $n(3) 1Mb 10ms DropTail
$ns duplex-link $n(0) $n(2) 1Mb 10ms DropTail
$ns duplex-link $n(2) $n(3) 1Mb 10ms DropTail
$ns duplex-link $n(3) $n(1) 1Mb 10ms DropTail

$ns duplex-link-op $n(0) $n(2) orient right 
$ns duplex-link-op $n(2) $n(3) orient left-down
$ns duplex-link-op $n(0) $n(3) orient right-down
$ns duplex-link-op $n(3) $n(1) orient left-down

set tcp [new Agent/TCP]
$ns attach-agent $n(3) $tcp 

set sink [new Agent/TCPSink]
$ns attach-agent $n(2) $sink
$ns connect $tcp $sink 
$tcp set fid_ 3 

set ftp [new Application/FTP]
$ftp attach-agent $tcp 
$ftp set type_ FTP 


set udp0 [new Agent/UDP]
$ns attach-agent $n(0) $udp0 
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500 
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0
set null0 [new Agent/Null]
$ns attach-agent $n(2) $null0 
$ns connect $udp0 $null0 

set udp1 [new Agent/UDP]
$ns attach-agent $n(1) $udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 set packetSize_ 500 
$cbr1 set interval_ 0.005
$cbr1 attach-agent $udp1

set null1 [new Agent/Null]
$ns attach-agent $n(3) $null1 
$ns connect $udp1 $null1

$udp0 set fid_ 1
$udp1 set fid_ 2


$ns color 1 Blue
$ns color 2 Red
$ns color 3 Green

$ns at 0.1 "$cbr1 start"
$ns at 0.5 "$cbr0 start"
$ns at 4.0 "$cbr1 stop"
$ns at 3.5 "$cbr0 stop"
$ns at 1.0 "$ftp start"
$ns at 4.5 "$ftp stop"

$ns at 45 "finish"
$ns run
