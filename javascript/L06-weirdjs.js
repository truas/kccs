function weirdBehavior()
{
    var x = [0];
    console.log(x);
    //It should equal itself, which is good.
        console.log("Equals: " + (x==x));
        //document.write("Equals: " + (x==x));
        //window.alert((x==x))
    //But it also equals not itself, which is not so good
        console.log("Not equals: " + (x==!x));
    //What about comparing a 3 element array and a string
        var y = new Array(3);
        console.log("Array comparison: " + (y==",,"));
    
    //types
        
        console.log("NaN type of: " + typeof NaN);
        console.log("NaN equals NaN: " + (NaN == NaN));
        console.log("null type of: " + typeof null);
        console.log("null instance of object: " + (null instanceof Object));
        console.log("string instance of String: " + ("string" instanceof String));

    
    //bounds
        
        console.log("bounds: " + 9999999999999999);
        console.log("compare float numbers: " + (0.1+0.2==0.3));
        console.log("Max > Min: " + (Math.max() > Math.min()));
        console.log("Max < Min: " + (Math.max() < Math.min()));

    
    //Length of an array
        
        console.log([]);
        console.log(![]);
        console.log((!+[]+![]).length);
        console.log("(!+[]+[]+![]).length is: " + ((!+[]+[]+![]).length));

        
}