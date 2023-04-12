import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { DetailsComponent } from "./components/details/details.component";
import { FormComponent } from "./components/form/form.component";

const routes: Routes = [
  {
    path: "",
    component: FormComponent,
  },
  {
    path: "details/:name",
    component: DetailsComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
