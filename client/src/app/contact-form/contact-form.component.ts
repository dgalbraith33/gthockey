import { Component, OnInit, ViewChild } from '@angular/core';
import { RecaptchaComponent } from 'ng-recaptcha';

import { ContactForm } from './../api/contact';
import { environment } from './../../environments/environment';
import { ApiService } from '../api.service';

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
    console.log(this.model);
    this.apiService.postContactForm(this.model).subscribe(resp => {
      this.success = resp.success;
      this.errors = resp.errors;
      this.recaptcha.reset();
      if (this.success) {
        this.model = new ContactForm();
      }
    });
  }

  handleCorrectCaptcha(event: any) {
    console.log(event);
    console.log(this.model);
  }

}
