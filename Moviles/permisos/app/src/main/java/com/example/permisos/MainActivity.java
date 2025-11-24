package com.example.permisos;

import android.Manifest;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        int permisoSMS = ContextCompat.checkSelfPermission(this, Manifest.permission.SEND_SMS);
        if (permisoSMS == PackageManager.PERMISSION_GRANTED){
            Toast.makeText(this, "permiso sms concedido", Toast.LENGTH_SHORT).show();
        }else{
            Toast.makeText(this, "no ha sido concedido", Toast.LENGTH_SHORT).show();
        }

        int permisoBio = ContextCompat.checkSelfPermission(this, Manifest.permission.USE_BIOMETRIC);
        if (permisoBio == PackageManager.PERMISSION_GRANTED){
            Toast.makeText(this, "permiso BIOMETRICO concedido", Toast.LENGTH_SHORT).show();
        }else{
            Toast.makeText(this, "biometrico no ha sido concedido", Toast.LENGTH_SHORT).show();
        }

        int permisoMedia = ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_MEDIA_LOCATION);
        if (permisoMedia == PackageManager.PERMISSION_DENIED){
            int codigo_respuesta = 200;
            Toast.makeText(this, "permiso media no concedido", Toast.LENGTH_SHORT).show();
            requestPermissions(new String[]{Manifest.permission.ACCESS_MEDIA_LOCATION}, codigo_respuesta);
        }
    }
}