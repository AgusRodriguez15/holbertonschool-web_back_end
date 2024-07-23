export default function getListStudentIds(students) {

    if (!Array.isArray(students) || students.length === 0) {
        return [];
    }
    let studentIds = students.map(student => student.id);

    return studentIds;
}