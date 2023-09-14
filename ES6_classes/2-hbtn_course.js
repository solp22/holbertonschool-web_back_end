export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be string')
    }
    if (typeof length !== 'number') {
      throw TypeError('Length must be string')
    }
    if (!Array.isArray(students)) {
      throw TypeError('Students must be an array of strings')
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

  set setName(newName) {
    if (typeof newName !== 'string') {
      throw TypeError('Name must be string')
    }
    this._name = newName;
  }

  set setLength(newLength) {
    if (typeof newLength !== 'number') {
      throw TypeError('Length must be string')
    }
    this._length = newLength;
  }

  set setStudents(newStudents) {
    if (!Array.isArray(newStudents)) {
      throw TypeError('Students must be an array of strings')
    }
    this._students = newStudents;
  }
}
