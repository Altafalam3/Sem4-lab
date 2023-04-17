# create a simulator object
set ns [new Simulator]

# open Nam trace file
set nf [open out.nam w]
$ns namtrace-all $nf
set np [open out.tr w]
$ns trace-all $np

#Define a 'finish' procedure
proc finish {}
{
global ns nf np
$ns flush-trace
# close the NAM trace file
close $nf
#Execute NAM on Trace file
exec nam out.nam &
exit 0
}
# create two nodes
set n0 [$ns node]
set n1 [$ns node]

#create a link
$ns duplex-link $n0 $n1 2mb 10ns Drop Tail

#set size of queue
$ns queue-limit $n0 $n1 5

#monitor the queue 
$ns duplex-link-op $n0 $n1
queuepos 0.5

#set up TCP connection
set tcp[new agent/TCP]
$ns attachment $n0 $tcp
set sink[new agent/TCP sink]
$ns attachment $n1 sink
$ns connect $tcp sink

#set up FTP over TCP connection
set tcp[new Application/FTP]
$FTP attachment tcp

#Schedule an event for ftp
$ns at 0.1 "$FTP start"
$ns at 4.0 "$ftp stop"

#call the procedure to finish after 5s of time
$ns at 5.0 "finish"

#To run the file call ns
$ns  run
