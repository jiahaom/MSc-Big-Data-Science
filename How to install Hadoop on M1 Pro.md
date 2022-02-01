> successfully installed on the macOS Monterey v12.1/ Apple M1 Pro 2021


1. Install Parallels Destop 17 (https://www.parallels.com/uk/)

1. Install Ubuntu ARM64 on PD 17
Ubuntu on PD17

2. Follow the guide (https://qmplus.qmul.ac.uk/mod/page/view.php?id=1838361):

*2.1 replace all "hadoop-3.2.1" with "hadoop-3.2.2" from the link (https://phoenixnap.com/kb/install-hadoop-ubuntu)


3. follow the instructions until "Single Node Hadoop Deployment (Pseudo-Distributed Mode)" step.

 ls -la ~/ | more

There should be a .bashrc on the first page. 

*If not just create it with:  vi ~/.bashrc

to make it rw r r: chmod 644 .bashrc


4. continue the left steps in the guide without sudo, otherwise you will see:
hdoop is not in the sudoers file.  This incident will be reported.


5. use 

export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64

instead of export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64


6. if you see 

No such file or directory

on the "Start Hadoop Cluster" step, feel free to use followed lines instead:

'/home/hdoop/hadoop-3.2.2/sbin/start-dfs.sh' 
'/home/hdoop/hadoop-3.2.2/sbin/start-yarn.sh' 


7. Finally:

Ubuntu on PD 17



