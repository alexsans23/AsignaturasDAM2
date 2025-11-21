package com.arquitecturajava;


import com.arquitecturajava.model.Persona;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;


public class Prueba1JPA {

    public static void main(String[] args) {

        Persona yo = new Persona("Pedro", 25);
        EntityManagerFactory emf =
                Persistence.createEntityManagerFactory("UnidadPersonas");
        EntityManager em = emf.createEntityManager();

        try {
            em.getTransaction().begin();
            em.persist(yo);
            em.getTransaction().commit();
            System.out.println("todo ha ido biien");
        } catch (Exception e) {
            e.printStackTrace();
            if (em.getTransaction().isActive()) {
                em.getTransaction().rollback();
                System.out.println("desastre");
            }
        } finally {
            em.close();
            emf.close();
        }
    }
}