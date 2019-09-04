# coding:utf-8
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def awsIot(jsonData):
    # 初期化
    myMQTTClient = AWSIoTMQTTClient("raspi")

    # MQTTクライアントの設定
    myMQTTClient.configureEndpoint("xxxxx.iot.ap-northeast-1.amazonaws.com", 443)
    myMQTTClient.configureCredentials("./cert/AmazonRootCA1.pem", "./cert/xxxxx-private.pem.key", "./cert/xxxxx-certificate.pem.crt")
    myMQTTClient.configureOfflinePublishQueueing(-1)
    myMQTTClient.configureDrainingFrequency(2)
    myMQTTClient.configureConnectDisconnectTimeout(60)
    myMQTTClient.configureMQTTOperationTimeout(60)

    # Connect to AWS IoT endpoint and publish a message
    myMQTTClient.connect()
    print ("Connected to AWS IoT")
    myMQTTClient.publish("packetCollect/jimsyo", jsonData , 0)
    myMQTTClient.disconnect()
