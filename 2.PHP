<?php

// 获取表单数据
$server_name = $_POST['server_name'];
$server_version = $_POST['server_version'];
$server_port = $_POST['server_port'];

// 构建命令行参数
$command = "java -jar 1.19.2.jar --port $server_port --world world --nogui";

// 创建一个新的 screen 会话，并在其中启动 Minecraft 服务器
exec("screen -dmS minecraft $command");

?>
