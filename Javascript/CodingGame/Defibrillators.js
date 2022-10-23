/**
 * https://www.codingame.com/ide/puzzle/defibrillators
 **/

 let lon = readline();
 let lat = readline();
 const N = parseInt(readline());
 
 let closest = null;
 let name    = '';
 
 function to_float(variable){
     return parseFloat(variable.replace(',', '.'));
 }
 
 lon = to_float(lon);
 lat = to_float(lat);
 
 for (let i = 0; i < N; i++) {
     let [, def_name, , , def_lon, def_lat] = readline().split(';');
 
     def_lon = to_float(def_lon);
     def_lat = to_float(def_lat);
     
     x = (def_lon - lon) * Math.cos((lat + def_lat) / 2.00);
     y = def_lat - lat;
     d = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)) * 6371.00;
 
     if (closest == null || d < closest){
         closest = d;
         name    = def_name;
     }
 }
 
 console.log(name);
 