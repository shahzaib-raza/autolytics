let my_dict = {
    "audi": [["a1", "A1"], ["a3", "A3"], ["a4", "A4"], ["a5", "A5"], ["a6", "A6"], ["a7", "A7"], ["a8", "A8"],
             ["e-tron", "e-tron"], ["q2", "Q2"], ["q3", "Q3"], ["q5", "Q5"], ["q7", "Q7"], ["r8", "R8"], ["tt", "Tt"]],

    "toyota": [["86", "86"], ["aqua", "Aqua"], ["Belta", "belta"], ["c-hr", "C-HR"], ["corolla", "Corolla"],
               ["camry", "Camry"], ["coaster", "Coaster"], ["corolla-axio", "Axio"], ["corona", "Corona"],
               ["corolla-cross", "Cross"], ["corolla-fielder", "Fielder"], ["crown", "Crown"], ["fortuner", "Fortuner"],
               ["hiace", "Hiace"], ["harrier", "Harrier"], ["hilux", "Hilux"], ["pixis", "Pixis"], ["premio", "Premio"],
               ["yaris", "Yaris"]],

    "united": [["alpha", "Alpha"], ["bravo", "Bravo"]],

    "daewoo": [["cielo", "Cielo"], ["matiz", "Matiz"], ["racer", "Racer"]],

    "daihatsu": [["atrai-wagon", "Atrai Wagon"], ["boon", "Boon"], ["charade", "Charade"], ["copen", "Copen"],
                 ["esse", "Esse"], ["hijet", "Hijet"], ["mira", "Mira"], ["move", "Move"], ["terios", "Terios"],
                 ["terios-kid", "Terios Kid"]],

    "datson": [["1000", "1000"], ["120y", "120Y"], ["1200", "1200"], ["510", "510"], ["bluebird", "Bluebird"],
               ["cherry", "Cherry"], ["coupe", "Coupe"]],

    "dfsk": [["c37", "C37"], ["convoy", "Convoy"], ["glory-580", "Glory 580"], ["rustam", "Rustam"],
             ["shahbaz", "shahbaz"]],

    "faw": [["carrier", "Carrier"], ["sirius", "Sirius"], ["v2", "V2"], ["vita", "Vita"], ["x-pv", "X-PV"]],

    "honda": [["accord", "Accord"], ["acty", "Acty"], ["acura", "Acura"], ["airwave", "Airwave"], ["br-v", "BR-V"],
              ["civic", "Civic"], ["cr-x", "Cr X"], ["cr-v", "CR-V"], ["cr-z", "CR-Z"], ["cross-road", "Cross Road"],
              ["fit", "Fit"], ["grace-hybrid", "Grace Hybrid"], ["insight", "Insight"], ["jazz", "Jazz"],
              ["n-box", "N Box"], ["n-one", "N One"], ["n-wgn", "N Wgn"], ["spike", "Spike"], ["vezel", "Vezel"],
              ["z", "Z"]],

    "hyundai": [["accent", "Accent"], ["coupe", "Coupe"], ["elantra", "Elantra"], ["excel", "Excel"], ["grace", "Grace"],
                ["santro", "Santro"], ["shehzore", "Shehzore"], ["sonata", "Sonata"], ["tucsan", "Tucsan"]],

    "kia": [["classic", "Classic"], ["grand-carnival", "Grand Carnival"], ["picanto", "Picanto"], ["pride", "Pride"],
            ["rio", "Rio"], ["spectra", "Spectra"], ["sportage", "Sportage"]],

    "mazda": [["Atenza", "Atenza"], ["axela", "Axela"], ["azwagon", "Azwagon"], ["flair", "Flair"], ["rx8", "RX8"],
              ["rx9", "RX9"]],

    "mg": [["3", "3"], ["hs", "HS"], ["zs", "Zs"]],

    "mitsubishi": [["colt", "Colt"], ["ek-custom", "EK Custom"], ["ek-sport", "EK Sport"], ["ek-wagon", "EK Wagon"],
                   ["hiace", "Hiace"], ["lancer", "Lancer"], ["mirage", "Mirage"], ["pajero", "Pajero"]],

    "nissan": [["120-y", "120 Y"], ["350z", "350Z"], [" ad-van", "AD Van"], ["caravan", "Caravan"],
               ["clipper", "Clipper"], ["dayz", "Dayz"], ["juke", "Juke"], ["march", "March"], ["moco", "Moco"],
               ["note", "Note"], ["sunny", "Sunny"]],

    "prince": [["k01", "K01"], ["k07", "K07"], ["pearl", "Pearl"]],

    "proton": [["saga", "Saga"], ["x50", "X50"], ["x70", "X70"]],

    "suzuki": [["alto", "Alto"], ["apv", "APV"], ["baleno", "Baleno"], ["carry", "Carry"], ["ciaz", "Ciaz"],
               ["every", "Every"], ["fx", "FX"], ["hustler", "Hustler"], ["jimny", "Jimny"], ["kei", "Kei"],
               ["liana", "Liana"], ["margalla", "Margalla"], ["ravi", "Ravi"], ["swift", "Swift"],
               ["wagon-r", "Wagon R"]],
};


function get_model(id1, id2){
    let s1 = document.getElementById(id1);
    let s2 = document.getElementById(id2);
    s2.innerHTML = "";
    let list =  my_dict[s1.value];
    for (let option in list){
        let newoption = document.createElement("option");
        newoption.value = list[option][0];
        newoption.innerHTML = list[option][1];
        s2.options.add(newoption);
    }
}

function main(){
    console.log(my_dict['suzuki']);
}