export default class Currency {
  constructor(name, code) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be string');
    }
    if (typeof code !== 'string') {
      throw TypeError('Code must be a number');
    }
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be string');
    }
    this._name = name;
  }

  set code(code) {
    if (typeof code !== 'string') {
      throw TypeError('Code must be string');
    }
    this._code = code;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`
  }
}
