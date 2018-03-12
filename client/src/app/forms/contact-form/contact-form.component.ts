import { Component, OnInit, ViewChild } from '@angular/core';

import { RecaptchaComponent } from 'ng-recaptcha';

import { environment } from './../../../environments/environment';
import { ApiService } from '../../api/api.service';
import { ContactForm } from './../../api/contact';

@Component({
  selector: 'app-contact-form',
  templateUrl: './contact-form.component.html',
  styleUrls: ['./contact-form.component.css']
})
export class ContactFormComponent implements OnInit {

  model = new ContactForm();
  @ViewChild(RecaptchaComponent) recaptcha: RecaptchaComponent;

  success: boolean;
  errors: any = {};

  readonly recaptchaKey = environment.recaptchaKey;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
  }

  submitForm() {
    this.apiService.postContactForm(this.model).subscribe(response => {
      this.success = true;
      this.errors = {};
      this.recaptcha.reset();
      this.model = new ContactForm();
    }, response => {
      this.success = false;
      this.errors = response.error.errors;
      this.recaptcha.reset();
    });
  }
}
