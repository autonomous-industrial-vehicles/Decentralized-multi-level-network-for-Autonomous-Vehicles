var Web3 = require("web3");
var express = require("express");
var app = express();
var server = require("http").createServer(app);

web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
server.listen(8080);

app.use(express.static("public"));

app.get("/", function(req, res){
        res.sendFile(__dirname + "/public/html/index.html");
})

var hashd = "0x68bc7ca0eE382Ae165466c9f65606291F1a8181f"; //smart contract registration hash address on the private Ethereum network.
var indexSmartContract = web3.eth.contract([{"constant":true,"inputs":[{"name":"key","type":"string"}],"name":"getSensor","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"key","type":"string"}],"name":"getOwner","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"key","type":"string"},{"name":"owner","type":"string"},{"name":"value","type":"uint256"},{"name":"sensor","type":"string"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"key","type":"string"}],"name":"getValue","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"key","type":"string"}],"name":"getData","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]) //Index to the smart contract for registration of autonomous elements

var SmartContract = indexSmartContract.at(hashd);

SmartContract.set.sendTransaction("hola","robot2",45,"Infrarrojo",{from: web3.eth.accounts[0]})
