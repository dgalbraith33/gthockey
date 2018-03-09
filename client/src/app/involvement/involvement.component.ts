import { Component, OnInit, ViewChild } from '@angular/core';
import { InvolvementForm } from '../api/involvement';
import { RecaptchaComponent } from 'ng-recaptcha';
import { environment } from '../../environments/environment';
import { ApiService } from '../api.service';

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
    this.apiService.postInvolvementForm(this.model).subscribe(resp => {
      this.success = resp.success;
      this.errors = resp.errors;
      this.recaptcha.reset();
      if (this.success) {
        this.model = new InvolvementForm();
      }
    });
  }
}
