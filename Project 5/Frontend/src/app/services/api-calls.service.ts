import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { LaureateDetails } from "../utilities/details.interface";
import { FilterDetails } from "../utilities/filter.interface";
@Injectable({
  providedIn: "root",
})
export class ApiCallsService {
  baseURL = "http://localhost:8000";
  constructor(private httpClient: HttpClient) {}

  get(uri: string): Observable<string[]> {
    const url = this.baseURL + uri;
    return this.httpClient.get<string[]>(url);
  }

  getDetails(uri: string): Observable<LaureateDetails> {
    const url = this.baseURL + uri;
    return this.httpClient.get<LaureateDetails>(url);
  }

  setItems(filterDetails: FilterDetails): void {
    localStorage.setItem("filters", JSON.stringify(filterDetails));
  }

  getItems(key: string) {
    let returnData = <FilterDetails>{};
    if (localStorage.getItem(key) !== null) {
      const temp = localStorage.getItem(key);
      returnData =
        temp !== null
          ? JSON.parse(temp)
          : { category: "", year: "", country: "" };
    }
    return returnData;
  }
}
