export default function createReportObject(employeesList) {
  const reportObject = {
    [allEmployees]: employeesList,
    getNumberOfDepartments(employeesList) {
      return employeesList.length
    },
  };
  return reportObject;
}
