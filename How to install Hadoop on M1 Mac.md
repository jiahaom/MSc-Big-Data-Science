> successfully installed on the macOS Monterey v12.1/ Apple M1 Pro 2021

# Introduction
- Install Hadoop on Single Machine/Pseudo-Distributed Mode

# Installation
1. Install [Parallels Destop 17](https://www.parallels.com/uk/)

2. Install Ubuntu ARM64 on PD 17
<img width="873" alt="Screenshot 2022-02-01 at 10 04 19" src="https://user-images.githubusercontent.com/32929553/151955793-3762ba4b-1095-4272-b140-36084d99d9ea.png">

3. Follow the [How to Install Hadoop on Ubuntu 18.04 or 20.04](https://phoenixnap.com/kb/install-hadoop-ubuntu)

	3.1 Replace all "hadoop-3.2.1" with "hadoop-3.2.2"  based on the [Hadoop Version](https://hadoop.apache.org/releases.html)

4. On the **"Single Node Hadoop Deployment (Pseudo-Distributed Mode)"** step:
- `ls -la ~/ | more`

There should be a .bashrc on the first page. *If not just create it with: `vi ~/.bashrc`

- `chmod 644 .bashrc` to make it *rw r r*

5. On the **"Configure Hadoop Environment Variables (bashrc)"** :

use `export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native` instead.


6. Continue the left steps in the guide **without sudo**, otherwise you will see:

`hdoop is not in the sudoers file.  This incident will be reported.
`

7. On the **"Edit hadoop-env.sh File"** step:
use `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64
`

instead of `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-**amd64**`


8. On the **"Start Hadoop Cluster"** step:
if you see `No such file or directory
`
on the "Start Hadoop Cluster" step, feel free to use followed lines instead:

`'/home/hdoop/hadoop-3.2.2/sbin/start-dfs.sh' 
`

`'/home/hdoop/hadoop-3.2.2/sbin/start-yarn.sh' 
`

9. Finally:
<img width="1920" alt="Screenshot 2022-02-01 at 10 22 06" src="https://user-images.githubusercontent.com/32929553/151956920-e40ddd7e-2dd8-4c91-baf4-95ac307b5423.png">



