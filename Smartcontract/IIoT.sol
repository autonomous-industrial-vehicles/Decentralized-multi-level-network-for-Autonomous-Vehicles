// SPDX-License-Identifier: MIT
// compiler version must be greater than or equal to 0.5.0 and less than 0.6.0
pragma solidity ^0.5.0;
contract IIoT_Register{
    struct register{
        uint data;
        string owner;
        uint value;
        string sensor;
    }
    mapping (string => register) Info;
    function set(string memory key,string memory owner, uint value, string memory sensor) public{
       Info[key] = register(block.timestamp,owner,value,sensor);
    }
    function getData(string memory key) public view returns (uint){
        return Info[key].data;
    }
    function getOwner(string memory key) public view returns (string memory){
        return Info[key].owner;
    }
    function getValue(string memory key) public view returns (uint){
        return Info[key].value;
    }
    function getSensor(string memory key) public view returns (string memory){
        return Info[key].sensor;
    }

}
