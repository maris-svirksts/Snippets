class Queue {
    constructor() {
        this.enqueue_stack = [];
        this.dequeue_stack = [];
    }
    
    Enqueue(data) {
        this.enqueue_stack.push(data);
    }
    
    // Not sure what this 'stack' should hold, made it hold the last dequeued element.
    Dequeue() {
        this.dequeue_stack[0] = this.enqueue_stack.shift();
    }
    
    get print_first() {
        return this.enqueue_stack[0];
    }
}
  
function processData(input) {
    let queue = new Queue();
    let command, value, input_lines;
      
    input_lines = input.split("\n");
  
    input_lines.forEach((item) => {
        let input_array = item.split(' ');
        [command, value] = input_array;
  
        switch(command) {
            case '1':
                queue.Enqueue(value);
                break;
            case '2':
                queue.Dequeue();
                break;
            case '3':
                console.log(queue.print_first);
                break;
            default:
                // Do Nothing.
        }
    });
} 
  
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";

process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});  