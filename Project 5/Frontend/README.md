#Project 5 - Nobel Ontology Project

## Team Members:
1. Pooja Baba: Frontend
2. Ishu Goyal: Backend

## Angular Project 
1. Open the project in an IDE.
2. run `npm install` to install the dependencies from the package.json file.
3. After executing the above command, run command `ng serve --open` to serve the project. 
4. This will open a new tab in the browser with the home page of the project

## Project details
1. First page that will be loaded is the homepage of the project. This page consists of a form that consists of the following filters - 
    1. Country
    2. Year
    3. Category
2. You can select a value from the above filter by clicking on the dropdown. Once you click on the dropdown API is called to retrive the data for that filter.
3. You can also search for a value in the dropdown to select a specific value.
4. Once you select a value and want to see the data for that filter, you can click on the Search button at the botton of the filters. By default this will be disabled, since there are no values selected.
5. Upon clicking on the Search button, a loading indicator will be shown indicating that an API call has been made to retrieve the data and once data has been retrieved, the loading indicator will be replaced with the result of the API call.
6. If the API call returns an empty data, then No Results found message will be displayed.
7. The results are the names of the nobel laureates based on the filters selected. You can click on a name in the list displayed in the results section to see more details about the laureate.
8. You will be redirected to a new page. Once you land on a new page, an API call will be made to to fetch the details of the name clicked on, on the previous page. 
9. Once the details are fetched, you will be shown the details of the nobel laureate. Image of the nobel laureate also will be displayed based on the photo url receveid in the response. However, if the photo URL is broken, then a default image will be displayed.
10. There is a Back button on the details page that will alow you to go to the previous page.
11. Once you land on the homepage after clicking the Back button in the details page, the filters will be displayed and the results corresponding to the the filters will also be displayed in the results section.
