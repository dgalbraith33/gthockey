import { Component, OnInit, ViewChild } from '@angular/core';
import { ProspectForm } from '../api/prospect';
import { environment } from '../../environments/environment';
import { RecaptchaComponent } from 'ng-recaptcha';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-prospect-form',
  templateUrl: './prospect-form.component.html',
  styleUrls: ['./prospect-form.component.css']
})
export class ProspectFormComponent implements OnInit {

  model = new ProspectForm();
  @ViewChild(RecaptchaComponent) recaptcha: RecaptchaComponent;

  success: boolean;
  errors: any = {};

  readonly recaptchaKey = environment.recaptchaKey;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
  }

  submitForm() {
    console.log(this.model);
    this.apiService.postProspectForm(this.model).subscribe(resp => {
      this.success = resp.success;
      this.errors = resp.errors;
      this.recaptcha.reset();
      if (this.success) {
        this.model = new ProspectForm();
      }
    });
  }
}
