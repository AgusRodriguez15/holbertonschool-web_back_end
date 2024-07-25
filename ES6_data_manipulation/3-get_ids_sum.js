export default function getStudentIdsSum(students) {
  const contador = 0;
  const sumContador = students.reduce(
    (accumulator, currentValue) => accumulator + currentValue.id,
    contador,
  );
  return sumContador;
}
