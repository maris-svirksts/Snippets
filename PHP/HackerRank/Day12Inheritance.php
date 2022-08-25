<?php
class person {
    protected $firstName, $lastName, $id;
    
    public function __construct($first_name, $last_name, $identification) {
        $this->firstName = $first_name;
        $this->lastName = $last_name;
        $this->id = $identification;
    }
    
    function printPerson() {
        print("Name: {$this->lastName}, {$this->firstName}\n");
        print("ID: {$this->id}\n");
    }
}
class Student extends person {
    private $testScores;
	protected $firstName;
	protected $lastName;
	protected $id;
	protected $scores;
  
    /*	
    *   Class Constructor
    *   
    *   Parameters:
    *   firstName - A string denoting the Person's first name.
    *   lastName - A string denoting the Person's last name.
    *   id - An integer denoting the Person's ID number.
    *   scores - An array of integers denoting the Person's test scores.
    */
    // Write your constructor here
    function __construct($first_name, $last_name, $id, $scores) {
        $this->firstName = $first_name;
        $this->lastName  = $last_name;
        $this->id         = $id;
        $this->scores     = $scores;
    }
    /*	
    *   Function Name: calculate
    *   Return: A character denoting the grade.
    */
    // Write your function here
	function calculate() {
		$result = array_sum($this->scores) / count($this->scores);
		
		if ( $result >= 90 ) {
			$return = "O";
		} else if ( $result >= 80 ) {
			$return = "E";
		} else if ( $result >= 70 ) {
			$return = "A";
		} else if ( $result >= 55 ) {
			$return = "P";
		} else if ( $result >= 40 ) {
			$return = "D";
		} else {
			$return = "T";
		}
		
		return $return;
	}
}


$file = fopen("php://stdin", "r");

$name_id = explode(' ', fgets($file));

$first_name = $name_id[0];
$last_name = $name_id[1];
$id = (int)$name_id[2];

fgets($file);

$scores = array_map(intval, explode(' ', fgets($file)));

$student = new Student($first_name, $last_name, $id, $scores);

$student->printPerson();

print("Grade: {$student->calculate()}");