from utilidades import change_pkl


file =     r"C:\Users\Principal\Documents\proyectos tt\proyecto_hermana_hugo.pkl"
new_file = r"C:\Users\Principal\Documents\proyectos tt\proyecto_hermana_hugo_res.pkl"
key = "path"
value = r"C:\Users\Principal\Documents\proyectos tt\casa_hermana_de_hugo.png"

change_pkl(file, new_file, key, value)