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
    this.apiService.postProspectForm(this.model).subscribe(resp => {
      this.success = true;
      this.errors = {};
      this.recaptcha.reset();
      this.model = new ProspectForm();
    }, response => {
      this.success = false;
      this.errors = response.error.errors;
      this.recaptcha.reset();
    });
  }
}
