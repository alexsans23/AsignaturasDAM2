package com.naciones;


import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

import java.util.List;

import com.naciones.model.Country;

public class CRUD {
    public static void main(String[] args) {
        EntityManagerFactory emf = null;
        EntityManager em = null;

        try {
            emf = Persistence.createEntityManagerFactory("Naciones");
            em = emf.createEntityManager();

            // ---- CREATE (introducimos dos paises)----
            em.getTransaction().begin();
            Country c1 = new Country("Suiza", 12345.5, "AD", "RTU");
            em.persist(c1);
            Country c2 = new Country("España", 12876.0, "SD", "EWR");
            em.persist(c2);
            em.getTransaction().commit();
            System.out.println("CREADO: " + c1);
            System.out.println("CREADO: " + c2);

            // ---- READ (listamos todos) ----
            List<Country> list1 = em.createQuery("SELECT c FROM Country c", Country.class).getResultList();
            System.out.println("LISTADO: ");
            for (Country c : list1) {
                System.out.println(c);
            }


            // ---- UPDATE ----
            em.getTransaction().begin();
            Country toUpdate = em.find(Country.class, c1.getCountryId());
            if (toUpdate != null) {
                toUpdate.setName("Noruega");
            }
            em.getTransaction().commit();
            System.out.println("ACTUALIZADO: " + toUpdate);

            // ---- READ individual ----
            Country found = em.find(Country.class, c1.getCountryId());
            System.out.println("FIND por id: " + found);

            // ---- DELETE ----
            em.getTransaction().begin();
            Country toRemove = em.find(Country.class, c1.getCountryId());
            if (toRemove != null) {
                em.remove(toRemove);
                System.out.println("BORRADO: id=" + c1.getCountryId());
            } else {
                System.out.println("No encontrado para borrar id=" + c1.getCountryId());
            }
            em.getTransaction().commit();

            // ---- READ final ----
            List<Country> listFinal = em.createQuery("SELECT c FROM Country c", Country.class).getResultList();
            System.out.println("LISTADO FINAL: tamaño=" + listFinal.size());
            for (Country c : listFinal) {
                System.out.println(c);
            }


        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // cerrar EntityManager y EntityManagerFactory correctamente
            if (em != null && em.isOpen()) em.close();
            if (emf != null && emf.isOpen()) emf.close();
        }
    }
}
