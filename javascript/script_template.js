var global = 20;
function init()
{    
    //Print something
    //*************
        // console.log("Hallo Welt");
        // window.alert("Hallo Welt");
        // document.getElementById("header").innerHTML = "Hallo Welt";
    
    //*************
    //Explain variables
    //*************
        var x = 5 + 6.5;
            //console.log("x:" + x);    
        var name = "Max " + "Mustermann";
            //console.log("name: " + name);    
        var combine = name + x;
            //console.log("combine: " + combine);    
        var fraction ={numerator: 5, denominator: 2};        
            //console.log(fraction);
    
        //Hands-On-Session
            //var z = 2 + 3 + "5";
            //console.log("z: " + z);
        
        //operators
    
        var compare = true;
        if(compare == false)
        {
            var tester = 3;
            console.log(compare || true);        
        }
    
        //Explain arrays
            //arrays();
    
        //Explain scope of variables
            var local = 50;
            //variables();
    //*************
    
    //Accessing HTML documents
        var header = document.getElementById("header");
        var first = document.getElementsByClassName("first");
        // console.log(first[0]);
        // header.setAttribute("style","color:red");
        // header.setAttribute("style","text-align:right");
        // header.setAttribute("style","color:red; text-align:right");
    
    //Application example
    //*************
        //createTable();
    
    //*************
    
    //Weird Behavior
        //weirdBehavior();
    
}
//Explain arrays
function arrays()
{
    //var cars = new Array("Volvo", "BMW");
    var cars = ["Volvo", "BMW"];	// Array
    var firstCar = cars[0];			// Get the first element
    console.log(firstCar);
    var sumCars = cars.length;		// Get the length of the array
    console.log(sumCars);
    cars[1] = "Mercedes";			// Assign new entry 
    console.log(cars)
    cars.push("Audi");			    // Adds new entry to the end
    console.log(cars);
    var audi = cars.pop();			// Removes the last element
    console.log(audi);
    console.log(cars);
    var volvo = cars.shift();		// Removes the first element
    console.log(cars);
    cars.unshift("VW");             // Adds new entry to the front
    console.log(cars);
    
    //***********************
    //strange behavior:
    var parse = "5";
        console.log(parseInt(parse) + 10);
    
    var maths = [1, 2, 9];
        console.log(maths.map(Math.sqrt));
    
    var strange = ["10", "10", "10"];
        console.log(strange.map(parseInt));
    
    
    //***********************
}

//Explain global and local variables
function variables()
{
    var local = 10;
    console.log(global + local);
}
//Create a table dynamically
function createTable()
{
    //initialize some data to put in the table
    var items = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]];
    items[1][1]=10;
    //Get the table from the index.html file
    var table = document.getElementById("table");
    
    for(var i = 0; i < items.length; i++)
    {
        //Create elements
        var tr = document.createElement("tr");
        var sum = 0;
        for(var j = 0; j < items[0].length; j++)
        {
            var td = document.createElement("td");
            //Important to add text nodes. There is no attribute 'text'
            var textNode = document.createTextNode(items[i][j]);
            sum = sum + parseInt(items[i][j]);
            //Append nodes in the hierarchy
            td.appendChild(textNode);
            tr.appendChild(td);        
        }
        //Calculate the sum and add another td element
        var td = document.createElement("td");
        td.setAttribute("style","border-width:2px; border-color:red; border-style:solid;");

        //show difference between createTextNode and innherHTML
            var textNode = document.createTextNode(sum);
                //var textNode = document.createTextNode("<b>" + sum + "</b>");
            td.appendChild(textNode);      
                //td.innerHTML = "<b>" + sum + "</b>";
        tr.appendChild(td);        
        
        //finally add the tr element which contains all td elements to the table
        table.appendChild(tr);
    }
    
    //set some attributes for the table
    table.setAttribute("style","border-width:2px; border-color:black; border-style:solid; text-align:center;");           
}
//Triggered by a click event
function divPressed(a)
{
    //Get a random number
    var randomX = Math.round(Math.random()*800);
    //set Position of the DIV
    a.setAttribute("style","position:absolute; left:"+ randomX+"px; background-color:red; width:90px");
}
//Some weird examples
function weirdBehavior()
{
    var x = [0];
    console.log(x);
    //It should equal itself, which is good.
        console.log("Equals: " + (x==x));
        //document.write("Equals: " + (x==x));
    //But it also equals not itself, which is not so good
        console.log("Not equals: " + (x==!x));
    //What about comparing a 3 element array and a string
        var y = new Array(3);
        console.log("Array comparison: " + (y==",,"));
    
    //types
        /*
        console.log("NaN type of: " + typeof NaN);
        console.log("NaN equals NaN: " + (NaN == NaN));
        console.log("null type of: " + typeof null);
        console.log("null instance of object: " + (null instanceof Object));
        console.log("string instance of String: " + ("string" instanceof String));
        */
    
    //bounds
        /*
        console.log("bounds: " + 9999999999999999);
        console.log("compare float numbers: " + (0.1+0.2==0.3));
        console.log("Max > Min: " + (Math.max() > Math.min()));
        console.log("Max < Min: " + (Math.max() < Math.min()));
        */
    
    //Length of an array
        /*
        console.log([]);
        console.log(![]);
        console.log((!+[]+![]).length);
        console.log("(!+[]+[]+![]).length is: " + ((!+[]+[]+![]).length));
        */
}