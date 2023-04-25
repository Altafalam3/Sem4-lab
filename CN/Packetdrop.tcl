set ns [new Simulator]

$ns color 1 Blue
$ns color 2 Red

set nf [open prac4.nam w]
$ns namtrace-all $nf

proc finish {} {
global ns nf
$ns flush-trace
close $nf
exec nam prac4.nam &
exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

$ns duplex-link $n0 $n2 20Mb 10ms DropTail 
$ns duplex-link $n1 $n2 20Mb 10ms DropTail
$ns duplex-link $n3 $n2 5Mb 10ms DropTail

$ns queue-limit $n2 $n3 5

$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right

$ns duplex-link-op $n2 $n3 queuePos 1

set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink
$ns connect $tcp $sink

$tcp set fid_ 1

set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP
$ftp set rate_ 1mb

set udp [new Agent/UDP]
$ns attach-agent $n1 $udp
set null [new Agent/Null]
$ns attach-agent $n3 $null
$ns connect $udp $null

$udp set fid_ 2

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate_ 1mb

$ns at 1.0 "$ftp start"
$ns at 1.5 "$cbr start"
$ns at 2.0 "$ftp stop"
$ns at 3.0 "$cbr stop"

$ns at 5.0 "finish"

$ns run