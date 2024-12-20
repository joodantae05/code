import tkinter as tk
import time  # Pour mesurer le temps de scan

class StatsPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.config(bg="#1E1E2D")  # Fond sombre, cohérent avec HomePage et DashboardPage
        self.frame = tk.Frame(root, bg="#1E1E2D")  # Fond sombre également pour le cadre

        # Ajouter un label pour les statistiques
        self.stats_label = tk.Label(self.frame, text="Statistiques du Scan", fg="white", bg="#1E1E2D", font=("Arial", 18, "bold"))
        self.stats_label.pack(pady=30)  # Espacement pour donner de l'air autour du titre
        
        # Ajouter un label pour les statistiques de scan (données fictives ici pour exemple)
        self.total_scans_label = tk.Label(self.frame, text="Total de scans effectués: 0", fg="white", bg="#1E1E2D", font=("Arial", 14))
        self.total_scans_label.pack(pady=10)  # Espacement entre les informations

        self.avg_scan_time_label = tk.Label(self.frame, text="Temps moyen de scan: 0s", fg="white", bg="#1E1E2D", font=("Arial", 14))
        self.avg_scan_time_label.pack(pady=10)

        self.most_vulnerable_host_label = tk.Label(self.frame, text="Hôte le plus vulnérable: Aucun", fg="white", bg="#1E1E2D", font=("Arial", 14))
        self.most_vulnerable_host_label.pack(pady=10)

        # Variables pour le calcul des statistiques
        self.total_time = 0  # Temps total de tous les scans effectués
        self.scan_count = 0  # Nombre total de scans effectués
        self.most_vulnerable_host = "Aucun"  # Par défaut, pas d'hôte vulnérable

    def show(self):
        """Afficher la page des statistiques"""
        self.frame.pack(fill='both', expand=True)

    def hide(self):
        """Masquer la page des statistiques"""
        self.frame.pack_forget()

    def update_stats(self, total_scans, avg_scan_time, most_vulnerable_host):
        """Mettre à jour les statistiques affichées après chaque scan"""
        self.total_scans_label.config(text=f"Total de scans effectués: {total_scans}")
        self.avg_scan_time_label.config(text=f"Temps moyen de scan: {avg_scan_time}s")
        self.most_vulnerable_host_label.config(text=f"Hôte le plus vulnérable: {most_vulnerable_host}")
    
    def scan(self):
        """Simuler un scan et mettre à jour les statistiques"""
        start_time = time.time()  # Enregistrer le début du scan
        
        # Simulation de scan (remplacez ceci par la logique réelle de scan)
        time.sleep(2)  # Exemple : simuler un scan de 2 secondes
        
        end_time = time.time()  # Fin du scan
        scan_time = end_time - start_time  # Temps écoulé pour ce scan
        
        # Exemple de détection d'un hôte vulnérable (remplacez ceci par votre logique de détection réelle)
        vulnerable_host = "192.168.1.100"  # Par exemple, un hôte vulnérable trouvé
        
        # Mettre à jour les statistiques après ce scan
        self.update_stats(scan_time, vulnerable_host)

# Exemple d'utilisation de StatsPage
if __name__ == "__main__":
    root = tk.Tk()
    app = None  # Remplacez ceci par votre app réelle si nécessaire
    stats_page = StatsPage(root, app)

    stats_page.show()  # Afficher la page des statistiques
    stats_page.scan()  # Effectuer un scan et mettre à jour les stats
    stats_page.scan()  # Effectuer un autre scan et mettre à jour les stats
    root.mainloop()
