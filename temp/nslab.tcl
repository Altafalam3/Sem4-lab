set ns [new Simulator]
set nf [open out.nam w]
$ns namtrace-all $nf
set tr [open out.tr w]
$ns trace-all $tr
proc finish {} {
global nf ns tr
$ns flush-trace
close $tr
exec nam out.nam &
exit 0
}
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

$n0 label "D"
$n1 label "C"
$n2 label "A"
$n3 label "B"

$ns duplex-link $n0 $n1 10Mb 20ms DropTail
$ns duplex-link $n0 $n2 10Mb 20ms DropTail
$ns duplex-link $n1 $n3 10Mb 20ms DropTail
$ns duplex-link $n3 $n2 10Mb 20ms DropTail
$ns duplex-link $n0 $n3 10Mb 20ms DropTail

$ns queue-limit $n0 $n1 10
$ns queue-limit $n1 $n3 10
$ns queue-limit $n0 $n2 10
$ns queue-limit $n3 $n2 10
$ns queue-limit $n0 $n3 10

$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n0 $n2 orient down
$ns duplex-link-op $n1 $n3 orient down
$ns duplex-link-op $n3 $n2 orient left
$ns duplex-link-op $n0 $n3 orient right-down




set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
set ftp [new Application/FTP]
$ftp attach-agent $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink
set udp [new Agent/UDP]
$ns attach-agent $n2 $udp
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
set null [new Agent/Null]
$ns attach-agent $n3 $null
$ns connect $tcp $sink
$ns connect $udp $null
$ns rtmodel-at 1.0 down $n1 $n3
$ns rtmodel-at 2.0 up $n1 $n3
$ns rtproto LS
$ns at 0.0 "$ftp start"
$ns at 0.0 "$cbr start"
$ns at 5.0 "finish"
$ns run
