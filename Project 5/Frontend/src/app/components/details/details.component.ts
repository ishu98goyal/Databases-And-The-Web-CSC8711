import { Component, OnInit } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { ApiCallsService } from "src/app/services/api-calls.service";
import { GET_DETAILS } from "src/app/utilities/constants";
import { LaureateDetails } from "src/app/utilities/details.interface";

@Component({
  selector: "app-details",
  templateUrl: "./details.component.html",
  styleUrls: ["./details.component.scss"],
})
export class DetailsComponent implements OnInit {
  nobelLaureateDetails = <LaureateDetails>{};
  loadingData: boolean = false;
  constructor(
    private route: ActivatedRoute,
    private apiCalls: ApiCallsService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.fetchDetails(params["name"]);
    });
  }

  fetchDetails(nobelLaureateName: string): void {
    this.loadingData = true;
    this.apiCalls
      .getDetails(GET_DETAILS.replace("name", nobelLaureateName))
      .subscribe({
        next: (details: LaureateDetails) => {
          this.loadingData = false;
          this.nobelLaureateDetails = details;
        },
        error: (err) => {
          this.loadingData = false;
          console.error("Cannot fetch the details");
        },
      });
  }
}
