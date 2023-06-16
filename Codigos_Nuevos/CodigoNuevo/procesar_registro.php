<?php
// Obtener los datos del formulario de registro
$username = $_POST['username'];
$email = $_POST['email'];
$password = $_POST['password'];

// Validar los datos ingresados (ejemplo básico)
if (empty($username) || empty($email) || empty($password)) {
    echo "Por favor, complete todos los campos.";
    exit;
}

// Redireccionar al usuario al formulario de inicio de sesión
header("Location: MiniMarket/InisioSesion.html");
exit;
?>


<?php
// Obtener los datos del formulario de inicio de sesión
$username = $_POST['username'];
$password = $_POST['password'];

// Validar los datos ingresados (ejemplo básico)
if (empty($username) || empty($password)) {
    echo "Por favor, ingrese su nombre de usuario y contraseña.";
    exit;
}

// Si las credenciales son correctas, iniciar la sesión y redireccionar al usuario a la página de inicio
session_start();
$_SESSION['username'] = $username;
header("Location: MiniMarket/Pag_Princ.html");
exit;
?>

