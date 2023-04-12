import { Component, OnInit } from "@angular/core";
import { ApiCallsService } from "src/app/services/api-calls.service";
import {
  GET_YEARS,
  GET_CATEGORIES,
  GET_COUNTRIES,
  COUNTRIES_LOADING_TEXT,
  YEARS_LOADING_TEXT,
  CATEGORIES_LOADING_TEXT,
  YEAR,
  CATEGORY,
  COUNTRY,
  YEAR_CATEGORY,
  YEAR_COUNTRY_CATEGORY,
  COUNTRY_CATEGORY,
} from "src/app/utilities/constants";
import { Router } from "@angular/router";

@Component({
  selector: "app-form",
  templateUrl: "./form.component.html",
  styleUrls: ["./form.component.scss"],
})
export class FormComponent implements OnInit {
  countries: Array<String> = [];
  categories: Array<String> = [];
  years: Array<String> = [];
  winners: Array<String> = [];
  selectedCountry: any = null;
  selectedCategory: any = null;
  selectedYear: any = null;
  loadingResult: boolean = false;
  isSearchClicked: boolean = false;
  loading = {
    countries: {
      message: COUNTRIES_LOADING_TEXT,
      loading: false,
    },
    years: {
      message: YEARS_LOADING_TEXT,
      loading: false,
    },
    categories: {
      message: CATEGORIES_LOADING_TEXT,
      loading: false,
    },
  };
  readonly loadingText: string = COUNTRIES_LOADING_TEXT;
  constructor(private apiCalls: ApiCallsService, private router: Router) {}

  ngOnInit(): void {
    const filters = this.apiCalls.getItems("filters");
    console.log(filters);
    if (filters["category"] !== "") {
      this.selectedCategory = filters["category"];
    }
    if (filters["year"] !== "") {
      this.selectedYear = filters["year"];
    }
    if (filters["country"] !== "") {
      this.selectedCountry = filters["country"];
    }
    if (this.selectedYear || this.selectedCountry || this.selectedCategory) {
      this.searchData();
    }
  }

  // when dropdown opened
  dropdownOpened(whichDropdown: string) {
    switch (whichDropdown) {
      case "country": {
        if (this.countries.length === 0) {
          this.loading.countries.loading = true;
          this.apiCalls.get(GET_COUNTRIES).subscribe(
            (data) => {
              setTimeout(() => {
                this.countries = data;
                this.loading.countries.loading = false;
              }, 1000);
            },
            (err) => {
              this.loading.countries.loading = false;
              console.error("Cannot fetch data");
            }
          );
        }

        break;
      }
      case "year": {
        if (this.years.length === 0) {
          this.loading.years.loading = true;
          this.apiCalls.get(GET_YEARS).subscribe(
            (data) => {
              setTimeout(() => {
                this.years = data;
                this.loading.years.loading = false;
              }, 1000);
            },
            (err) => {
              this.loading.years.loading = false;
              console.error("Cannot fetch data");
            }
          );
        }
        break;
      }
      case "category": {
        if (this.categories.length === 0) {
          this.loading.categories.loading = true;
          this.apiCalls.get(GET_CATEGORIES).subscribe({
            next: (data) => {
              setTimeout(() => {
                this.categories = data;
                if (data) {
                  this.categories = data.map(
                    (category) =>
                      category.charAt(0).toUpperCase() + category.slice(1)
                  );
                }
                this.loading.categories.loading = false;
              }, 1000);
            },
            error: (err) => {
              this.loading.categories.loading = false;
              console.error("Cannot fetch data");
            },
          });
        }

        break;
      }
    }
  }

  // handleData
  handleData(data: Array<string>): void {
    setTimeout(() => {
      if (data.length === 0) {
        this.isSearchClicked = true;
      } else {
        this.isSearchClicked = false;
      }
      this.winners = data;
      this.loadingResult = false;
    }, 1500);
  }

  // when clicked on search button
  searchData() {
    const filters = {
      category: this.selectedCategory ? this.selectedCategory : "",
      year: this.selectedYear ? this.selectedYear : "",
      country: this.selectedCountry ? this.selectedCountry : "",
    };
    this.apiCalls.setItems(filters);

    // year, country and category selected
    if (this.selectedYear && this.selectedCategory && this.selectedCountry) {
      this.loadingResult = true;
      this.apiCalls
        .get(
          YEAR_COUNTRY_CATEGORY.replace("year", this.selectedYear)
            .replace("category", this.selectedCategory)
            .replace("country", this.selectedCountry)
        )
        .subscribe({
          next: (data) => {
            this.handleData(data);
          },
        });
    }
    // year and country selected
    else if (this.selectedYear && this.selectedCountry) {
      this.loadingResult = true;
      this.apiCalls
        .get(
          YEAR_CATEGORY.replace("year", this.selectedYear).replace(
            "country",
            this.selectedCountry
          )
        )
        .subscribe({
          next: (data) => {
            this.handleData(data);
          },
        });
    }
    // country and category selected
    else if (this.selectedCountry && this.selectedCategory) {
      this.loadingResult = true;
      this.apiCalls
        .get(
          COUNTRY_CATEGORY.replace("country", this.selectedCountry).replace(
            "country",
            this.selectedCountry
          )
        )
        .subscribe({
          next: (data) => {
            this.handleData(data);
          },
        });
    }
    // category and year selected
    else if (this.selectedCategory && this.selectedYear) {
      this.loadingResult = true;
      this.apiCalls
        .get(
          YEAR_CATEGORY.replace("year", this.selectedYear).replace(
            "category",
            this.selectedCategory
          )
        )
        .subscribe({
          next: (data) => {
            this.handleData(data);
          },
        });
    }
    // only year selected
    else if (this.selectedYear) {
      this.loadingResult = true;
      this.apiCalls.get(YEAR.replace("year", this.selectedYear)).subscribe({
        next: (data) => {
          this.handleData(data);
        },
      });
    }
    // only category selected
    else if (this.selectedCategory) {
      this.apiCalls
        .get(CATEGORY.replace("category", this.selectedCategory))
        .subscribe({
          next: (data) => {
            this.handleData(data);
          },
        });
    }
    // only country selected
    else if (this.selectedCountry) {
      this.loadingResult = true;
      this.apiCalls
        .get(COUNTRY.replace("country", this.selectedCountry))
        .subscribe({
          next: (data) => {
            this.handleData(data);
          },
        });
    }
  }
}
