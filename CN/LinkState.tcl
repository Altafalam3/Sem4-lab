set ns [new Simulator]

set nf [open lsr.nam w]
$ns namtrace-all $nf

$ns rtproto LS

proc finish {} {
global ns nf
$ns flush-trace
close $nf
exec nam lsr.nam &
exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]

$ns duplex-link $n0 $n1 10Mb 10ms DropTail
$ns duplex-link $n1 $n2 10Mb 10ms DropTail
$ns duplex-link $n2 $n3 10Mb 10ms DropTail
$ns duplex-link $n3 $n4 10Mb 10ms DropTail
$ns duplex-link $n4 $n0 10Mb 10ms DropTail
$ns duplex-link $n1 $n3 20Mb 10ms DropTail
$ns duplex-link $n1 $n4 20Mb 10ms DropTail

$ns duplex-link-op $n0 $n1 orient right-up
$ns duplex-link-op $n1 $n2 orient right-down
$ns duplex-link-op $n2 $n3 orient down
$ns duplex-link-op $n3 $n4 orient left
$ns duplex-link-op $n4 $n0 orient up
$ns duplex-link-op $n1 $n3 orient left-up
$ns duplex-link-op $n1 $n4 orient right-up

set tcp [new Agent/TCP]
$ns attach-agent $n1 $tcp
$tcp set Class_ 2

set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink

$ns connect $tcp $sink

set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP
$ftp set packet_size_ 1000
$ftp set rate_ 1Mb

$ns at 0.2 "$ftp start"
$ns rtmodel-at 0.5 down $n1 $n4
$ns rtmodel-at 1.5 up $n1 $n4
$ns at 1.8 "$ftp stop"
$ns at 2.0 "finish"

$ns run