import { Component, OnInit, ViewChild } from '@angular/core';

import { RecaptchaComponent } from 'ng-recaptcha';

import { environment } from '../../../environments/environment';
import { ApiService } from '../../api/api.service';
import { InvolvementForm } from '../../api/involvement';

@Component({
  selector: 'app-involvement',
  templateUrl: './involvement.component.html',
  styleUrls: ['./involvement.component.css']
})
export class InvolvementComponent implements OnInit {

  model = new InvolvementForm();
  @ViewChild(RecaptchaComponent) recaptcha: RecaptchaComponent;

  success: boolean;
  errors: any = {};

  readonly recaptchaKey = environment.recaptchaKey;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
  }

  submitForm() {
    this.apiService.postInvolvementForm(this.model).subscribe(response => {
      this.success = true;
      this.errors = {};
      this.recaptcha.reset();
      this.model = new InvolvementForm();
    }, response => {
      this.success = false;
      this.errors = response.error.errors;
      this.recaptcha.reset();
    });
  }
}
