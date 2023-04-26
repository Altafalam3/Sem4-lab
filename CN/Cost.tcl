set ns [new Simulator]
$ns rtproto DV

set nf [open tout.tr w]
$ns trace-all $nf
set np [open tout.nam w]
$ns namtrace-all $np

proc finish {} {
global ns np nf
$ns flush-trace 
close $nf
close $np
exec nam tout.nam &
exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]

$ns duplex-link $n0 $n2 10Mb 10ms DropTail 
$ns duplex-link $n0 $n1 10Mb 10ms DropTail 
$ns duplex-link $n0 $n3 10Mb 10ms DropTail 
$ns duplex-link $n3 $n2 10Mb 10ms DropTail 
$ns duplex-link $n1 $n3 10Mb 10ms DropTail 
$ns duplex-link $n3 $n4 10Mb 10ms DropTail 

$ns queue-limit $n0 $n2 10
$ns queue-limit $n0 $n1 10
$ns queue-limit $n0 $n3 10
$ns queue-limit $n3 $n2 10
$ns queue-limit $n1 $n3 10
$ns queue-limit $n3 $n4 10

$ns duplex-link-op $n0 $n2 orient right
$ns duplex-link-op $n0 $n1 orient down
$ns duplex-link-op $n0 $n3 orient right-down
$ns duplex-link-op $n3 $n2 orient up
$ns duplex-link-op $n1 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right

$n0 label "A"
$n1 label "B"
$n2 label "C"
$n3 label "D"
$n4 label "E"

$ns cost $n0 $n1 11
$ns cost $n0 $n2 1 
$ns cost $n0 $n3 27 
$ns cost $n3 $n2 2 
$ns cost $n0 $n3 3 
$ns cost $n3 $n4 1

set tcp [new Agent/TCP]
$tcp set fid_ 1
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink
$ns connect $tcp $sink

set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP
$ftp set packetSize_ 1000
$ftp set rate_ 1mb

$ns color 1 red
$ns at 1.0 "$ftp start"
$ns rtmodel-at 1.5 down $n2 $n3 
$ns rtmodel-at 2.5 up $n2 $n3
$ns at 3.0 "$ftp stop"

$ns at 5.0 "finish"

$ns run
