package com.example.emailapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText etTo;
    private EditText etSubject;
    private EditText etBody;
    private Button btnSend;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etTo = findViewById(R.id.et_to);
        etSubject = findViewById(R.id.et_subject);
        etBody = findViewById(R.id.et_body);
        btnSend = findViewById(R.id.btn_send);

        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String to = etTo.getText().toString().trim();
                String subject = etSubject.getText().toString().trim();
                String body = etBody.getText().toString().trim();

                if (to.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Introduce al menos un destinatario", Toast.LENGTH_SHORT).show();
                    return;
                }

                Intent intent = new Intent(Intent.ACTION_SEND);
                intent.setType("message/rfc822"); // MIME para email
                intent.putExtra(Intent.EXTRA_EMAIL, new String[]{ to }); // array de destinatarios
                intent.putExtra(Intent.EXTRA_SUBJECT, subject);
                intent.putExtra(Intent.EXTRA_TEXT, body);

                if (intent.resolveActivity(getPackageManager()) != null) {
                    startActivity(Intent.createChooser(intent, "Enviar email..."));
                } else {
                    Toast.makeText(MainActivity.this, "No hay app de correo instalada (rfc822)", Toast.LENGTH_LONG).show();
                }
            }
        });

    }
}
