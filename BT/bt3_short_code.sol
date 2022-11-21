// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

import "hardhat/console.sol";
contract MS{
    struct Student{
        int256 ID;
        string name;
        int256 marks;
    }
    int256 public stdCount=0;
    mapping(int256=>Student) public stdRecords;
    function addNewRecords(int256 ID, string memory name, int256 marks) public{
        stdCount+=1;
        stdRecords[stdCount]=Student(ID,name,marks);
    }
    fallback() external{
        console.log("fallback func called");
    }
}