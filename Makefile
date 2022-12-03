run:
	geth --http --http.corsdomain="http://localhost:8080" --http.api web3,eth,debug,personal,net --vmdebug --datadir data-chain --dev console

install_ubuntu:
	sudo add-apt-repository -y ppa:ethereum/ethereum && sudo apt-get update && sudo apt-get install ethereum
	
install_fedora:
	sudo dnf install -y make.x86 golang.x86  git.x86 && git clone https://github.com/ethereum/go-ethereum && cd go-ethereum && make geth
