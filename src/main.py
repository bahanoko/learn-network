from flask import Flask, request, jsonify,render_template
from scapy.all import sniff, IP, UDP, DNS

app = Flask(__name__)

# DNSパケットをキャプチャする
def capture_dns():
    packets = sniff(filter="udp port 53", count=10, timeout=10)
    results = []
    for packetNum,packet in enumerate(packets,start=1):
        results.append({
            "number":packetNum,
            "result":packet.summary()
        })

    return results

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dns_capture")
def dns_capture():
    dns_datas = capture_dns()
    return jsonify(dns_datas)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
