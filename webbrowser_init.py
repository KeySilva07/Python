import webbrowser

urls = [
        "https://panorama.ufpi.br/zabbix.php?action=map.view&sysmapid=3",
        "https://chat.ufpi.br/home",
        "https://redminedes.ufpi.br/",
        "https://mail.google.com/mail/u/0/#inbox",
        ]
for url in urls:
    webbrowser.open(url)