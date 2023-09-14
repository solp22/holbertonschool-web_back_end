export default class HolbertonCourse {
  constructor(name, length, students) {
    if(typeof name === 'string'){
      this._name = name;
    };
    if(typeof length === 'number'){
      this._length = length;
    };
    if(Array.isArray(students) && students.every(element => typeof element === 'string')){
      this._students = students;
    };
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
    this._name = newName;
  }

  set setLength(newLength) {
    this._length = newLength;
  }

  set setStudents(newStudents) {
    this._students = newStudents;
  }
}
