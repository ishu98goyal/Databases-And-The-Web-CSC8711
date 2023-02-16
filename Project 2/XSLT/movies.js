function loadXMLDoc(filename) {
  console.log(filename);
  if (window.ActiveXObject) {
    xhttp = new ActiveXObject("Msxml2.XMLHTTP");
  }
  else {
    xhttp = new XMLHttpRequest();
  }
  xhttp.open("GET", filename, false);
  //try {xhttp.responseType = "msxml-document"} catch(err) {} // Helping IE11
  xhttp.send("");
  return xhttp.responseXML;
}




function displayMovies() {
  xml = loadXMLDoc("movies.xml");
  console.log(xml);
  xsl = loadXMLDoc("page1.xsl");
  console.log(xsl);
  // code for IE
  if (window.ActiveXObject || xhttp.responseType == "msxml-document") {
    ex = xml.transformNode(xsl);
    document.getElementById("journal_div").innerHTML = ex;
  }
  // code for Chrome, Firefox, Opera, etc.
  else if (document.implementation && document.implementation.createDocument) {
    xsltProcessor = new XSLTProcessor();
    xsltProcessor.importStylesheet(xsl);
    resultDocument = xsltProcessor.transformToFragment(xml, document);
    document.getElementById("journal_div").appendChild(resultDocument);
  }
}

function displayMovieBoth()
{
  displayMovie("t");
  displayMovie("T");
}

function displayMovie(m) {
  xml = loadXMLDoc("movies.xml");
  console.log(m);
  xsl = loadXMLDoc("page2.xsl");
  console.log(xsl);
  // code for IE
  if (window.ActiveXObject || xhttp.responseType == "msxml-document") {
    ex = xml.transformNode(xsl);
    document.getElementById("volume_div").innerHTML = ex;
  }
  // code for Chrome, Firefox, Opera, etc.
  else if (document.implementation && document.implementation.createDocument) {
    xsltProcessor = new XSLTProcessor();
    xsltProcessor.importStylesheet(xsl);
    xsltProcessor.setParameter(null,"m",m);
    resultDocument = xsltProcessor.transformToFragment(xml, document);
    console.log(resultDocument);
    console.log("removing number_div");
    e = document.getElementById("number_div")
    while (e.hasChildNodes()) {
      console.log("Hello");
      e.removeChild(e.firstChild);
    }
    e = document.getElementById("volume_div")
    while (e.hasChildNodes()) {
      e.removeChild(e.firstChild);
    }
    e.appendChild(resultDocument);
  }
}

function displayDetails(name) {
  console.log(name);
  xml = loadXMLDoc("movies.xml");
  console.log(xml);
  xsl = loadXMLDoc("page3.xsl");
  console.log(xsl);
  // code for IE
  if (window.ActiveXObject || xhttp.responseType == "msxml-document") {
    ex = xml.transformNode(xsl);
    document.getElementById("number_div").innerHTML = ex;
  }
  // code for Chrome, Firefox, Opera, etc.
  else if (document.implementation && document.implementation.createDocument) {
    xsltProcessor = new XSLTProcessor();
    xsltProcessor.importStylesheet(xsl);
    xsltProcessor.setParameter(null,"name",name);
    resultDocument = xsltProcessor.transformToFragment(xml, document);
    console.log(resultDocument);
    e = document.getElementById("number_div")
    while (e.hasChildNodes()) {
      e.removeChild(e.firstChild);
    }
    e.appendChild(resultDocument);
  }
}

