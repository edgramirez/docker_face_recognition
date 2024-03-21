{
    "configuration":
    {
        "clientId": "0001",
        "ZG916V4W70016QK":
        {
            "cameraName": "Tlahuac",
            "source": "file:///home/kayros/amlo.mp4",
            "source": "rtsp://192.168.120.9:9000/live",
            "services": [
                            {
                            "whiteList": {
                                "enabled": true,
                                "dbName": "/home/kayros/dbs/whitelist/camara_1.dat",
                                "endpoint": "http://127.0.0.1:8000/posts/blackAndWhite"
                                }
                            },
                            {
                            "blackList": {
                                "enabled": true,
                                "dbName": "/home/kayros/dbs/blacklist/camara_1.dat",
                                "endpoint": "http://127.0.0.1:8000/posts/blackAndWhite"
                                }
                            }
                        ]
        }
    }
}

