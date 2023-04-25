set ns [new Simulator]

$ns rtproto DV

set nf [open out1.nam w]
$ns namtrace-all $nf
set np [open out1.tr w]
$ns trace-all $np

proc finish { } {
global ns nf np
$ns flush-trace
close $nf
exec nam out1.nam &
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
$tcp set class_ 2
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink
$ns connect $tcp $sink 

set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP
$ftp set packet_size_ 1000
$ftp set rate_ 1mb
$ns at 1.0 "$ftp start"
$ns rtmodel-at 2.0 down $n0 $n3
$ns rtmodel-at 3.0 up $n0 $n3 
$ns at 4.0 "$ftp stop"

$ns at 5.0 "finish"

$ns run


 
