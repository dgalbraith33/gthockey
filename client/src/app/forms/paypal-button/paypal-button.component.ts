import { Component, OnInit, AfterViewChecked, Input } from '@angular/core';

import { CartService } from '../../cart/cart.service';

declare let paypal: any;

@Component({
  selector: 'app-paypal-button',
  templateUrl: './paypal-button.component.html',
  styleUrls: ['./paypal-button.component.css']
})
export class PaypalButtonComponent implements OnInit, AfterViewChecked {

  public didPaypalScriptLoad = false;

  public readonly paypalConfig: any = {
    env: 'sandbox', // Or 'production',
    client: {
      sandbox: 'AQpJXTQX-ocXqeXXbBM4X-mQXSu4nM5FefibPFfeCttr1PdRj8xZLwqA-dpRbmeNyxghwILT2Y0ynYgt',
      production: 'AV-yWn2S6YxORyIr6BqyghjhW29NOpfidTAEewcRp_822NEgZNwrfX-axZnw_a_qJfNv7Kb90jgtOt9g',
    },
    commit: true, // Show a 'Pay Now' button
    style: {
      color: 'gold',
      size: 'large'
    },
    payment: function(data, actions) {
      return actions.payment.create({
        payment: {
          transactions: [
            { amount: {total: this.cartService.totalCost(), currency: 'USD'}}
          ]
        }
      });
    },

    onAuthorize: function(data, actions) {
      /*
       * Execute the payment here
       */
    },

    onCancel: function(data, actions) {
      /*
       * Buyer cancelled the payment
       */
    },

    onError: function(err) {
      /*
       * An error occurred during the transaction
       */
    }
  };

  constructor(private cartService: CartService) { }

  ngOnInit() {
  }

  public ngAfterViewChecked(): void {
    if (!this.didPaypalScriptLoad) {
      this.loadPaypalScript().then(() => {
        paypal.Button.render(this.paypalConfig, '#paypal-button');
      });
    }
  }

  public loadPaypalScript(): Promise<any> {
    this.didPaypalScriptLoad = true;
    return new Promise((resolve, reject) => {
      const scriptElement = document.createElement('script');
      scriptElement.src = 'https://www.paypalobjects.com/api/checkout.js';
      scriptElement.onload = resolve;
      document.body.appendChild(scriptElement);
    });
  }
}

