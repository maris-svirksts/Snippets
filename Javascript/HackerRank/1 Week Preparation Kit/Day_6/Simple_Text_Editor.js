// https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/problem

class TextEditor {
    constructor() {
        this.content  = '';
        this.previous = [];
    }
    
    Append(data) {
        this.previous.push(this.content);
        this.content = this.content + data;
    }
    
    Delete(length) {
        this.previous.push(this.content);

        let position = this.content.length - length;
        this.content = this.content.slice(0, position);
    }
    
    Print(position) {
        console.error(this.content, 'print');
        return this.content.charAt(position - 1);
    }
    
    Undo() {
        this.content = this.previous.pop();        
    }
}

function processData(input) {
    let queue = new TextEditor();
    let command, value, input_lines;
      
    input_lines = input.split("\n");

    input_lines.forEach((item) => {
        let input_array = item.split(' ');
        [command, value] = input_array;
  
        switch(command) {
            case '1':
                queue.Append(value);
                break;
            case '2':
                queue.Delete(parseInt(value));
                break;
            case '3':
                console.log(queue.Print(parseInt(value)));
                break;
            case '4':
                queue.Undo();
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