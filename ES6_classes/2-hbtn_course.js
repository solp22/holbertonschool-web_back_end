export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be string');
    }
    if (typeof length !== 'number') {
      throw TypeError('Length must be string');
    }
    if (!Array.isArray(students)) {
      throw TypeError('Students must be an array of strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get getName() {
    return this._name;
  }

  get getLength() {
    return this._length;
  }

  get getStudents() {
    return this._students;
  }

  set name(name) {
    if (typeof (name) !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = name;
  }

  set length(length) {
    if (typeof (length) !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = length;
  }

  set students(students) {
    if (!Array.isArray(students)) {
      throw TypeError('Students must be an array of strings');
    }
    this._students = students;
  }
}
