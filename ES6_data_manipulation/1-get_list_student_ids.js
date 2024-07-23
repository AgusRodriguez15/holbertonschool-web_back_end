export default function getListStudentIds(students) {
  if (!Array.isArray(students) || students.length === 0) {
    return [];
  }
  const studentIds = students.map((student) => student.id);

  return studentIds;
}
