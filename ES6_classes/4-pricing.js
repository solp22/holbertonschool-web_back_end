import Currency from "./3-currency";

export default class Pricing extends Currency {
  constructor(amount, currency) {
    this._amount = amount;
    super(currency)
  }

  get amount() {
    return this._amount;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set amount(amount) {
    this._amount = amount;
  }

  set code(code) {
    this._code = code;
  }

  set name(name) {
    this._name = name;
  }

  displayFullPrice() {
    return `${this._amount} ${this._name} (${this._code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
