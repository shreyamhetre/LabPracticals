// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract StudentData {
    struct Student {
        uint studentID;
        string name;
        uint age;
    }
    
    Student[] public students;


    event StudentAdded(uint studentID, string name, uint age);


    function addStudent(uint _studentID, string memory _name, uint _age) public {
        Student memory newStudent = Student(_studentID, _name, _age);
        students.push(newStudent);
        emit StudentAdded(_studentID, _name, _age);
    }


    receive() external payable {
        // Fallback function can accept Ether sent to the contract
        // You can implement additional logic here
    }
}
